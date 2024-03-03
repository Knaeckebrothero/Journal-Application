// Components
import { NavigationBarComponent } from './navbar/navigation-bar.component';
import { HeadBarComponent } from './head-bar/head-bar.component';
import { ActivitiesComponent } from './activities/activities.component';
import { RateComponent } from './rate/rate.component';
import { CommentComponent } from './comment/comment.component';

// Angular Material
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatListModule } from '@angular/material/list';
import { MatIconModule } from '@angular/material/icon';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatSelectModule } from '@angular/material/select';
import { MatAutocompleteModule } from '@angular/material/autocomplete';
import { MatButtonModule } from '@angular/material/button';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { MatSliderModule } from '@angular/material/slider';

// Base
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ServiceWorkerModule } from '@angular/service-worker';
import { RouterModule, Routes } from '@angular/router';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';


// Routes
const routes: Routes = [
  { path: 'activities', component: ActivitiesComponent },
  { path: 'rate', component: RateComponent },
  { path: 'comment', component: CommentComponent },
  { path: '', redirectTo: 'activities', pathMatch: 'full' }
];

@NgModule({
  declarations: [
    AppComponent,
    NavigationBarComponent,
    ActivitiesComponent,
    RateComponent,
    HeadBarComponent,
    CommentComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MatSidenavModule,
    MatListModule,
    MatIconModule,
    MatFormFieldModule,
    MatInputModule,
    FormsModule,
    ReactiveFormsModule,
    MatSelectModule,
    MatAutocompleteModule,
    MatButtonModule,
    MatCheckboxModule,
    MatSliderModule,
    RouterModule.forRoot(routes),
    ServiceWorkerModule.register('ngsw-worker.js', {
      registrationStrategy: 'registerWhenStable'
    }),
    BrowserAnimationsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
